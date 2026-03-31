from google.adk import Agent

root_agent = Agent(
    name="summarizer_agent",
    model="gemini-2.0-flash@latest",  # Vertex AI model name
    backend="vertexai",  # Use Vertex AI backend
    instruction="Summarize the user's text in 3 bullet points or fewer."
)