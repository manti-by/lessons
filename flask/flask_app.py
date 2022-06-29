import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def dict_to_str(data: dict) -> str:
    result = []
    for key, value in data.items():
        result.append(f"{key}: {value}")
    return ", ".join(result)


def dict_to_str_gen(data: dict) -> str:
    return ", ".join([
        f"{key}: {value}" for key, value in data.items()
    ])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info(
            dict_to_str(
                request.form.to_dict()
            )
        )
        return request.form.to_dict()

    logger.info(
        dict_to_str_gen(
            request.args.to_dict()
        )
    )
    return request.args.to_dict()


@app.route("/test/", methods=["GET"])
def test():
    return "Test URL"


if __name__ == "__main__":
    app.run()
