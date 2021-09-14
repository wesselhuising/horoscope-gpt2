from transformers import GPT2LMHeadModel, pipeline
from os import path


class Model:
    def __init__(self):
        self.pipeline = self.load_pipeline()

    def load_pipeline(self, model_path: str = "./app/model/"):
        if not path.isdir(model_path):
            raise Exception(f"path {model_path} is not a directory.")

        return pipeline(
            "text-generation",
            model=GPT2LMHeadModel.from_pretrained(model_path),
            tokenizer="GroNLP/gpt2-small-dutch",
        )

    def predict(self, context: str, max_length: int):
        context = context.strip()

        if not self.pipeline:
            raise Exception("Pipeline is not loaded.")

        horoscope = self.pipeline(context, max_length=max_length)

        if not horoscope[0]["generated_text"]:
            raise Exception("Generating text failed.")

        generated_text = horoscope[0]["generated_text"]

        if context.endswith("?"):
            generated_text = generated_text.replace(context, "")
        else:
            context = context + "..."

        return (context, generated_text.rsplit(".", 1)[0] + ".")


if __name__ == "__main__":
    model = Model()
    print(model.predict(context="Gaat er nog wat gebeuren vandaag?", max_length=100))
