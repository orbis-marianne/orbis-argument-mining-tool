"""
Hugging Face Pipelines to load the models.
"""

from django.conf import settings
from optimum.onnxruntime import ORTModelForTokenClassification, ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline


arguments_components_model = pipeline(
    task="token-classification",
    model=ORTModelForTokenClassification.from_pretrained(
        settings.ARGUMENTS_COMPONENTS_MODEL,
        export=True,
    ),
    tokenizer=AutoTokenizer.from_pretrained(
        settings.ARGUMENTS_COMPONENTS_MODEL,
        model_max_length=settings.ARGUMENTS_COMPONENT_MODEL_MAX_LENGTH,
    ),
    aggregation_strategy=settings.ARGUMENTS_COMPONENT_MODEL_STRATEGY,
    stride=settings.ARGUMENTS_COMPONENT_MODEL_STRIDE,
    batch_size=settings.MODELS_BATCH_SIZE,
)

arguments_relations_model = pipeline(
    task="text-classification",
    model=ORTModelForSequenceClassification.from_pretrained(
        settings.ARGUMENTS_RELATIONS_MODEL,
        export=True,
    ),
    tokenizer=AutoTokenizer.from_pretrained(
        settings.ARGUMENTS_RELATIONS_MODEL,
        model_max_length=settings.ARGUMENTS_RELATIONS_MODEL_MAX_LENGTH,
    ),
    batch_size=settings.MODELS_BATCH_SIZE,
)

statements_classification_model = pipeline(
    task="text-classification",
    model=ORTModelForSequenceClassification.from_pretrained(
        settings.STATEMENTS_CLASSIFICATION_MODEL,
        export=True,
    ),
    tokenizer=AutoTokenizer.from_pretrained(
        settings.STATEMENTS_CLASSIFICATION_MODEL,
        model_max_length=settings.STATEMENTS_CLASSIFICATION_MODEL_MAX_LENGTH,
    ),
    batch_size=settings.MODELS_BATCH_SIZE,
)

statements_relations_model = pipeline(
    task="text-classification",
    model=ORTModelForSequenceClassification.from_pretrained(
        settings.STATEMENTS_RELATIONS_MODEL,
        export=True,
    ),
    tokenizer=AutoTokenizer.from_pretrained(
        settings.STATEMENTS_RELATIONS_MODEL,
        model_max_length=settings.STATEMENTS_RELATIONS_MODEL_MAX_LENGTH,
    ),
    batch_size=settings.MODELS_BATCH_SIZE,
)
