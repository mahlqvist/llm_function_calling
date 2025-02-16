from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults

# Returns a quick summary of the search results as a concatenated string
simple_search = DuckDuckGoSearchRun()


# Returns search results in a structured format (output_format="json", output_format="list")
structured_search = DuckDuckGoSearchResults(output_format="list")

response = simple_search.invoke("What is Groq 3?")