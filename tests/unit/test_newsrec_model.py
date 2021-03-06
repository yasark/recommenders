# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import pytest
import os
from reco_utils.recommender.newsrec.newsrec_utils import prepare_hparams
from reco_utils.recommender.deeprec.deeprec_utils import download_deeprec_resources

from reco_utils.recommender.newsrec.models.nrms import NRMSModel
from reco_utils.recommender.newsrec.models.naml import NAMLModel
from reco_utils.recommender.newsrec.models.lstur import LSTURModel
from reco_utils.recommender.newsrec.models.npa import NPAModel
from reco_utils.recommender.newsrec.io.mind_iterator import MINDIterator
from reco_utils.recommender.newsrec.io.mind_all_iterator import MINDAllIterator


@pytest.fixture
def resource_path():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.mark.gpu
def test_nrms_component_definition(tmp):
    wordEmb_file = os.path.join(tmp, "utils", "embedding.npy")
    userDict_file = os.path.join(tmp, "utils", "uid2index.pkl")
    wordDict_file = os.path.join(tmp, "utils", "word_dict.pkl")
    yaml_file = os.path.join(tmp, "utils", r"nrms.yaml")

    if not os.path.exists(yaml_file):
        download_deeprec_resources(
            r"https://recodatasets.z20.web.core.windows.net/newsrec/",
            os.path.join(tmp, "utils"),
            "MINDdemo_utils.zip",
        )

    hparams = prepare_hparams(
        yaml_file,
        wordEmb_file=wordEmb_file,
        wordDict_file=wordDict_file,
        userDict_file=userDict_file,
        epochs=1,
    )
    iterator = MINDIterator
    model = NRMSModel(hparams, iterator)

    assert model.model is not None
    assert model.scorer is not None
    assert model.loss is not None
    assert model.train_optimizer is not None


@pytest.mark.gpu
def test_naml_component_definition(tmp):
    wordEmb_file = os.path.join(tmp, "utils", "embedding_all.npy")
    userDict_file = os.path.join(tmp, "utils", "uid2index.pkl")
    wordDict_file = os.path.join(tmp, "utils", "word_dict_all.pkl")
    vertDict_file = os.path.join(tmp, "utils", "vert_dict.pkl")
    subvertDict_file = os.path.join(tmp, "utils", "subvert_dict.pkl")
    yaml_file = os.path.join(tmp, "utils", r"naml.yaml")

    if not os.path.exists(yaml_file):
        download_deeprec_resources(
            r"https://recodatasets.z20.web.core.windows.net/newsrec/",
            os.path.join(tmp, "utils"),
            "MINDdemo_utils.zip",
        )

    hparams = prepare_hparams(
        yaml_file,
        wordEmb_file=wordEmb_file,
        wordDict_file=wordDict_file,
        userDict_file=userDict_file,
        vertDict_file=vertDict_file,
        subvertDict_file=subvertDict_file,
        epochs=1,
    )
    iterator = MINDAllIterator
    model = NAMLModel(hparams, iterator)

    assert model.model is not None
    assert model.scorer is not None
    assert model.loss is not None
    assert model.train_optimizer is not None


@pytest.mark.gpu
def test_npa_component_definition(tmp):
    wordEmb_file = os.path.join(tmp, "utils", "embedding.npy")
    userDict_file = os.path.join(tmp, "utils", "uid2index.pkl")
    wordDict_file = os.path.join(tmp, "utils", "word_dict.pkl")
    yaml_file = os.path.join(tmp, "utils", r"npa.yaml")

    if not os.path.exists(yaml_file):
        download_deeprec_resources(
            r"https://recodatasets.z20.web.core.windows.net/newsrec/",
            os.path.join(tmp, "utils"),
            "MINDdemo_utils.zip",
        )

    hparams = prepare_hparams(
        yaml_file,
        wordEmb_file=wordEmb_file,
        wordDict_file=wordDict_file,
        userDict_file=userDict_file,
        epochs=1,
    )
    iterator = MINDIterator
    model = NPAModel(hparams, iterator)

    assert model.model is not None
    assert model.scorer is not None
    assert model.loss is not None
    assert model.train_optimizer is not None


@pytest.mark.gpu
def test_lstur_component_definition(tmp):
    wordEmb_file = os.path.join(tmp, "utils", "embedding.npy")
    userDict_file = os.path.join(tmp, "utils", "uid2index.pkl")
    wordDict_file = os.path.join(tmp, "utils", "word_dict.pkl")
    yaml_file = os.path.join(tmp, "utils", r"lstur.yaml")

    if not os.path.exists(yaml_file):
        download_deeprec_resources(
            r"https://recodatasets.z20.web.core.windows.net/newsrec/",
            os.path.join(tmp, "utils"),
            "MINDdemo_utils.zip",
        )
    hparams = prepare_hparams(
        yaml_file,
        wordEmb_file=wordEmb_file,
        wordDict_file=wordDict_file,
        userDict_file=userDict_file,
        epochs=1,
    )
    iterator = MINDIterator
    model = LSTURModel(hparams, iterator)

    assert model.model is not None
    assert model.scorer is not None
    assert model.loss is not None
    assert model.train_optimizer is not None
