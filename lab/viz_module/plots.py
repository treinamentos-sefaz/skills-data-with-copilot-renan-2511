"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["rating"], bins=20, color="#722f37", edgecolor="white")
    ax.set_title("Distribuição das avaliações (rating)")
    ax.set_xlabel("Avaliação (rating)")
    ax.set_ylabel("Quantidade de vinhos")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    top = df["variety"].value_counts().head(10).sort_values()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(top.index.astype(str), top.values, color="#722f37")
    ax.set_title("Top 10 variedades de vinho")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade (variety)")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(5).index
    subset = df[df["variety"].isin(top_varieties)]
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(data=subset, x="variety", y="rating", order=list(top_varieties), ax=ax)
    ax.set_title("Avaliação (rating) por variedade — top 5")
    ax.set_xlabel("Variedade (variety)")
    ax.set_ylabel("Avaliação (rating)")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig
