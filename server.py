import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/VanitySoft/api/ca-boundaries-io'

mcp = FastMCP('ca-boundaries-io')

@mcp.tool()
def query_by_fsa_code(postal_fsa: Annotated[str, Field(description='Query by value postal code FSA, example: "A0A"')]) -> dict: 
    '''Query by Postal FSA ( example T6H )'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/fsa'
    headers = {'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'postal-fsa': postal_fsa,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_ldu_boundary_by_location_and_resolution(latitude: Annotated[Union[int, float], Field(description='Default: 46.04643887621965')],
                                                      longitude: Annotated[Union[int, float], Field(description='Default: -73.4532516514038')],
                                                      resolution: Annotated[Union[int, float, None], Field(description='Default: 10')] = None) -> dict: 
    '''Query for LDU H3 Boundary by Location and Resolution'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/h3/ldu/location/boundary'
    headers = {'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'resolution': resolution,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_ldu_boundary_by_h3index(h3ndex: Annotated[Union[int, float], Field(description='Default: 635775751926485600')]) -> dict: 
    '''Query for Boundary by H3Index. Query for a LDU boundary by H3 Index, if a LDU Postal Code does not exist within the H3 Index Hexagon, an empty FeatureCollection is returned. **H3Index resolution must be greater than 8.**'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/h3/ldu/index/635775751926485631'
    headers = {'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'h3ndex': h3ndex,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_ldu_boundary(postal_ldu: Annotated[str, Field(description='Query by LDU code.')],
                           resolution: Annotated[Union[int, float, None], Field(description='Default: 10')] = None) -> dict: 
    '''Query by a LDU Postal Code'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/ldu'
    headers = {'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'postal-ldu': postal_ldu,
        'resolution': resolution,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_city_names_by_province_territory_name(province: Annotated[str, Field(description='')]) -> dict: 
    '''Query for City names by province/territory name'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/province/city/names'
    headers = {'province': 'alberta', 'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'province': province,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_city_boundary_by_city_name(name: Annotated[str, Field(description='')]) -> dict: 
    '''Query for City Boundary by City name'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/province/city'
    headers = {'name': 'toronto', 'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_for_all_province_territory_names() -> dict: 
    '''Query for All Province / Territory names'''
    url = 'https://vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com/rest/v1/public/boundary/ca/province/name'
    headers = {'x-rapidapi-host': 'vanitysoft-canada-postal-boundaries-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
