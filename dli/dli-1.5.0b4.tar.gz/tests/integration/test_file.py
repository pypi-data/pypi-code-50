import pytest


@pytest.mark.integration
def test_download_datafile_on_windows(monkeypatch, client):
    # Make the test think that it is running on a Windows operating system.
    monkeypatch.setattr('os.name', 'nt')

    # ID of dataset that contains a very long path.
    datafile_id = '54a84860-5e06-11ea-b44e-1ec82ec268bd'
    datafile = client.get_datafile(datafile_id)
    dataset_id = datafile.dataset_id
    dataset = client.get_dataset(dataset_id)

    with pytest.raises(Exception) as e:
        dataset.download(destination_path='.')
    assert 'file name would be too long' in str(e.value)
