{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPpDId/RA5ntSLMSpM1KpNL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mzkhuzam2/STATS507/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "v3rsj1QDbEde",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 385
        },
        "outputId": "2e77f817-90e0-444f-f576-d4bce49b7978"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'dash'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-bd45e0a132f7>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mdash\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdash\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdcc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdash\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhtml\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexpress\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpx\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'dash'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import numpy as np\n",
        "import dash\n",
        "from dash import dcc\n",
        "from dash import html\n",
        "import plotly.express as px\n",
        "import pandas as pd\n",
        "\n",
        "app = dash.Dash(__name__)\n",
        "server = app.server\n",
        "\n",
        "# see https://plotly.com/python/px-arguments/ for more options\n",
        "df = pd.DataFrame({\n",
        "    \"Fruit\": [\"Apples\", \"Oranges\", \"Bananas\", \"Apples\", \"Oranges\", \"Bananas\"],\n",
        "    \"Amount\": [4, 1, 2, 2, 4, 5],\n",
        "    \"City\": [\"SF\", \"SF\", \"SF\", \"Montreal\", \"Montreal\", \"Montreal\"]\n",
        "})\n",
        "#df = pd.read_csv('flights.csv')\n",
        "\n",
        "fig = px.bar(df, x=\"Fruit\", y=\"Amount\", color=\"City\", barmode=\"group\")\n",
        "\n",
        "df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')\n",
        "\n",
        "fig2 = px.scatter(df2, x=\"gdp per capita\", y=\"life expectancy\",\n",
        "                 size=\"population\", color=\"continent\", hover_name=\"country\",\n",
        "                 log_x=True, size_max=60)\n",
        "\n",
        "app.layout = html.Div([\n",
        "    html.H1('Hello Dash'),\n",
        "\n",
        "    html.Div('''\n",
        "        Dash: A web application framework for your data.\n",
        "    '''),\n",
        "\n",
        "    dcc.Graph(\n",
        "        id='example-graph',\n",
        "        figure=fig\n",
        "    ),\n",
        "\n",
        "    html.Div('''\n",
        "        Dash: Another example for chart\n",
        "    '''),\n",
        "\n",
        "    dcc.Graph(\n",
        "        id='example-graph2',\n",
        "        figure=fig2\n",
        "    )\n",
        "])\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True, port=8080)\n"
      ]
    }
  ]
}