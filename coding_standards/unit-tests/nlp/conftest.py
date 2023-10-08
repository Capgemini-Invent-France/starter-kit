import pytest
import os
import pandas as pd

import nlp.config as config
from nlp.model_utils import load_model_joblib


@pytest.fixture()
def prod_model():
    path = os.path.join("../", config.PATH_MODEL)
    return load_model_joblib(path)


@pytest.fixture()
def path_prod_model():
    return os.path.join("../", config.PATH_MODEL)


@pytest.fixture()
def input_df():
    input_df = pd.DataFrame(
        {
            "titre": {
                3304: "MINT une société indescente !",
                4753: "ARNAQUE",
                2566: "MINT une société indescente !",
            },
            "verbatim": {
                3304: "Les tarifs ont quasiment doublé en six mois. Résiliation le 15 août 2022, prélèvement habituel en septembre 2022 ET idem EN OCTOBRE 2022. Cette société ne réponds pas aux questions, prélève des montants indus et se moque des abonnés bien malgré eux (transfert de OUI ELECTRIC)...",
                4753: "ARNAQUE\nFacture de 1200€ pour un 28 m2\nRésiliation faite par ENGIE le 28/03\n3 DOSSIERS DE RECLAMATION OUVERTS : AUCUN TRAITE\nau 01/06 la résiliation n'est toujours pas faite\nSERVICE CLIENT INCOMPETENT\nSERVICE RECLAMATION INEXISTANT\nj'ai HONTE pour vous",
                2566: "Les tarifs ont quasiment doublé en six mois. Résiliation le 15 août 2022, prélèvement habituel en septembre 2022 ET idem EN OCTOBRE 2022. Cette société ne réponds pas aux questions, prélève des montants indus et se moque des abonnés bien malgré eux (transfert de OUI ELECTRIC)...",
            },
            "date": {
                3304: "Date de l'expérience: 05 octobre 2022",
                4753: "Date de l'expérience: 01 juin 2022",
                2566: "Date de l'expérience: 05 octobre 2022",
            },
            "note": {
                3304: "Noté 1 sur 5 étoiles",
                4753: "Noté 1 sur 5 étoiles",
                2566: "Noté 1 sur 5 étoiles",
            },
            "fournisseur": {
                3304: "https://fr.trustpilot.com/review/www.mint-energie.com",
                4753: "https://fr.trustpilot.com/review/totalenergies.fr",
                2566: "https://fr.trustpilot.com/review/www.mint-energie.com",
            },
        }
    )

    return input_df


@pytest.fixture
def processed_df():
    sample_processed = pd.DataFrame(
        {
            "verbatim": {
                3304: "tarifs quasiment doublé six mois résiliation 15 août 2022 prélèvement habituel septembre 2022 idem octobre 2022 cette société réponds questions prélève montants indus moque abonnés bien malgré transfert oui electric",
                4753: "arnaque facture 1200€ 28 m2 résiliation faite 2803 3 dossiers reclamation ouverts aucun traite 0106 résiliation nest toujours faite service client incompetent service reclamation inexistant jai honte",
            },
            "note": {3304: 1.0, 4753: 1.0},
            "fournisseur": {3304: "www", 4753: "totalenergies"},
            "year": {3304: 2022, 4753: 2022},
            "month": {3304: 10, 4753: 6},
        }
    )

    return sample_processed
