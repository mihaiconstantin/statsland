# Standard library imports.
import io
import base64

# Matplotlib imports.
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Numpy imports.
import numpy as np


# Define dummy class for a student question information.
class Question:
    # Private fields.
    _prompt = None
    _response = None

    # Public fields.
    variable1 = None
    variable2 = None
    context = None
    concept = None
    useAi = True


    # Scatter plot.
    def _createScatterPlotFigure(self, xAxisTitle, yAxisTitle):
        # Generate some random data.
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2

        # Create the figure.
        figure = Figure()
        axis = figure.add_subplot(1, 1, 1)
        axis.scatter(x, y, s=area, c=colors, alpha=0.5)

        # Add titles to the axes.
        axis.set_xlabel(xAxisTitle)
        axis.set_ylabel(yAxisTitle)

        # Return the figure.
        return figure


    # Constructor.
    def __init__(self, variable1, variable2, context, concept, useAi):
        self.variable1 = variable1
        self.variable2 = variable2
        self.context = context
        self.concept = concept
        self.useAi = useAi


    # Craft question.
    def craftQuestion(self, client):
        # Construct prompt based on question information.
        self._prompt = "".join([
            "Please construct a question based on the following information:",
            "\n\n",
            "- the variables of interest are: '", self.variable1, "' and '", self.variable2, "'.",
            "\n",
            "- the context indicated by the student is: '", self.context, "'.",
            "\n",
            "- the statistical concept the student is trying to master is: '", self.concept, "'."
        ])


        # Obtain a question via the `OpenAI` API.
        self._response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                { "role": "system", "content": "".join([
                        "You are a helpful assistant aiding students to prepare for statistics exams in social statistics.",
                        "The response MUST consist only of the research hypothesis, without quotation marks, and no other information.",
                        "It is crucial to ONLY provide responses in the form of a detailed research hypothesis in line with the student's request.",
                        "Avoid speculative language such as \"The research hypothesis could be...\" and provide a clear, concise hypothesis statement."
                    ])
                },
                { "role": "user", "content": self._prompt }
            ]
        )


    # Generate visualization.
    def getVisualization(self):
        # Return a visualization (e.g., a scatter plot for the sake of example).
        figure = self._createScatterPlotFigure(self.variable1, self.variable2)

        # Render the figure.
        output = io.BytesIO()
        FigureCanvas(figure).print_png(output)

        # Encode the image.
        encoded_image = base64.b64encode(output.getvalue()).decode('utf-8')

        # Return a response as an image.
        return f"data:image/png;base64, { encoded_image }"


    # Get question.
    def getQuestion(self):
        if self._response is None:
            return "Question could not be crafted."
        else:
            # Extract the question from the response.
            return self._response.choices[0].message.content
