import yaml
import argparse
from jinja2 import Template


def generate(model_id: str = 'gpt-4o'):
    # Load the modelcard template into a string
    with open('scripts/modelcard-template.md', 'r', encoding='utf-8') as f:
        template_str = f.read()

    # Load the modelcard context into a dictionary
    try:
        modelcard_context_path = f'modelcard-data/{model_id}.yml'
        with open(modelcard_context_path, 'r', encoding='utf-8') as f:
            context = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Please make sure you have the modelcard context referenced at: {modelcard_context_path}")

    # Render the template with the model context
    template = Template(template_str)
    rendered = template.render(context)

    # Write the rendered modelcard to a markdown file
    with open(f'{model_id}-modelcard.md', 'w', encoding='utf-8') as f:
        f.write(rendered)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a model card.")
    parser.add_argument('model_id', type=str, help="The ID of the model to generate the card for")
    args = parser.parse_args()

    generate(args.model_id)