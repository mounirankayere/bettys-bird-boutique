import os
from google.cloud import discoveryengine_v1 as discoveryengine
from google.adk.tools import tool

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
DATASTORE_ID = os.environ.get("DATASTORE_ENGINE_ID")

def search(query: str) -> list[str]:
    client = discoveryengine.SearchServiceClient()
    serving_config = client.serving_config_path(
        project=PROJECT_ID,
        location=LOCATION,
        data_store=DATASTORE_ID,
        serving_config="default_config",
    )
    
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=query,
        page_size=5,
        content_search_spec=discoveryengine.SearchRequest.ContentSearchSpec(
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                return_snippet=True
            )
        ),
    )
    
    response = client.search(request)
    results = []
    for result in response.results:
        document = result.document
        snippet = document.derived_struct_data.get("snippets", [{}])[0].get("snippet", "")
        if snippet:
            results.append(snippet)
    return results

@tool
def search_store_documents(query: str) -> str:
    """Recherche des informations internes sur la boutique (horaires, histoire, personnel) dans les documents PDF."""
    snippets = search(query)
    if not snippets:
        return "Aucune information trouvée dans les documents de la boutique."
    return "\n".join(snippets)
