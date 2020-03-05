# coding: utf-8
"""Módulo para tabulaciones de lingüística y transformación de texto."""

import pandas as pd


def df_palabras(docs):
    """Crea DataFrame de palabras en corpus.

    Parameters
    ----------
    docs : Iterable[dict (text: str, tokens: list, meta: dict)]
        Anotaciones lingüísticas de cada frase.

    Returns
    -------
    pd.DataFrame
        Anotaciones lingüísticas de cada palabra.
    """
    dfs = []
    for frase in docs:
        df = pd.DataFrame(frase.get("tokens"))
        for k, v in frase.get("meta").items():
            df[k] = v

        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def df_frases(docs):
    """Crea DataFrame de frases en corpus.

    Parameters
    ----------
    docs : Iterable[dict (text: str, tokens: list, meta: dict)]
        Anotaciones lingüísticas de cada frase.

    Returns
    -------
    pd.DataFrame
        Texto y Metadata de cada frase.
    """
    df = pd.DataFrame(frase.get("meta") for frase in docs)
    df["text"] = [frase.get("text") for frase in docs]

    return df


def df_ngramas(ngramed):
    """Crea DataFrame de n-gramas en corpus.

    Parameters
    ----------
    ngramed : Iterable[tuple (list, dict (text: str, tokens: list, meta: dict))]
        Palabras y n-gramas de cada frase, y Anotaciones lingüísticas.

    Returns
    -------
    pd.DataFrame
        N-gramas y metadata de frase.
    """
    dfs = []
    for tokens, frase in ngramed:
        df = pd.DataFrame({"token": tokens})
        for k, v in frase.get("meta").items():
            df[k] = v

        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def df_probables(modelo, n=15):
    """Distribución de probabilidad de tokens en tópicos de modelo.

    Parameters
    ----------
    modelo : gensim.models.ldamodel.LdaModel
    n : int optional
        Cuantos tokens incluir.

    Returns
    -------
    pd.DataFrame
        Tokens probables de cada tópico y sus probabilidades.
    """
    dfs = []
    for topico in range(modelo.num_topics):
        data = modelo.show_topic(topico, n)
        df = pd.DataFrame(data=data, columns=["token", "probabilidad"])
        df["topico"] = topico
        dfs.append(df)

    df_topicos = pd.concat(dfs, ignore_index=True)

    return df_topicos.sort_values(
        by=["topico", "probabilidad"], ascending=[True, False]
    )
