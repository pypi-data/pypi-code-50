from pathlib import Path
from tempfile import NamedTemporaryFile
from click import echo, progressbar
from git import Blob
from ..defines import DATA_DIR, DATE_START
from ..people import MAYOR, SUSPECTS
from ..utils import wrap_paragraphs
from ..fillers import random_paragraphs, random_ids
from ..git_utils import git_commit, restore_head

COMMIT_MSG_INVESTIGATIONS = """\
This branch holds investigations.

You could *try* sifting through it, but it's probably better to know what you're looking for.
"""

def build_phase_3(repo, addresses):
    blob_ids = random_ids()
    blobs = []
    commit_investigation_path = Path(repo.working_tree_dir) / 'investigate'
    for (street_name, street_residents) in addresses.items():
        with restore_head(repo):
            # Detach head from current commit. We want only the tag to lead to the "house" commits.
            repo.head.reference = repo.commit('HEAD')
            assert repo.head.is_detached

            # Iterate in reverse so that house number N will be the tag's N-th parent.
            # The `+1` is because we also count the creation of the tag.
            with progressbar(length=len(street_residents) + 1,
                    label=f'Generating street commits: {street_name}') as bar:
                for (i, person) in enumerate(reversed(street_residents)):
                    if person in SUSPECTS:
                        suspect_index = SUSPECTS.index(person) + 1
                        interview_path = DATA_DIR / f'interview-{suspect_index}.txt'
                        interview = interview_path.read_text()
                        investigation_path = DATA_DIR / f'investigation-{suspect_index}.txt'
                        investigation_text = investigation_path.read_text()
                    else:
                        interview = random_paragraphs()
                        investigation_text = random_paragraphs()

                    # We generate a new blob to be added to the 'investigations' branch later on.
                    # We have to have the contents under an actual reference, otherwise they won't
                    # be cloned along with the repository by the player.
                    with NamedTemporaryFile('w') as investigation_file:
                        investigation_file.write(wrap_paragraphs(investigation_text))
                        investigation_file.flush()
                        blobs.append(Blob(
                            repo,
                            bytes.fromhex(repo.git.hash_object('-w', investigation_file.name)),
                            mode=Blob.file_mode,
                            path=str(next(blob_ids))))

                    commit_investigation_path.write_text(blobs[-1].hexsha)
                    repo.index.add(commit_investigation_path.as_posix())

                    git_commit(repo, MAYOR, DATE_START,
                        f'{len(street_residents) - i} {street_name}',
                        interview)
                    bar.update(1)

                # Create the tag to the "beginning" of the street.
                git_commit(repo, MAYOR, DATE_START, f'{street_name}')
                street_tag_name = street_name.lower().replace(' ', '_')
                repo.create_tag(f'street/{street_tag_name}')
                bar.update(1)

            for (i, suspect) in enumerate(SUSPECTS):
                if suspect in street_residents:
                    house_number = street_residents.index(suspect) + 1
                    echo(f'  Suspect #{i + 1} lives at #{house_number}')

    # Create a new branch, not connected to the repository's root, which will hold the
    # investigations texts' commits. If we don't place those commits somewhere addressable, when
    # the player `git clone`-s the repository they won't get them and cannot solve the mystery.
    echo('Creating the investigations branch')
    with restore_head(repo):
        repo.git.checkout('--orphan', 'investigations')
        repo.index.remove('*', force=True, working_tree=True)
        repo.index.add(blobs)
        git_commit(repo, MAYOR, DATE_START,
            'Investigations',
            COMMIT_MSG_INVESTIGATIONS)
