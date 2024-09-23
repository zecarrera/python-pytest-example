import logging

def before_all(context):
    logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

def after_step(context, step):
    if step.status == "failed":
        logging.error(f"Step failed: {step.name}")
        logging.error(f"Error message: {context.failed_step.exception}")
