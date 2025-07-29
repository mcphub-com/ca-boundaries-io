markdown
# ca-boundaries-io MCP Server

## Overview

The `ca-boundaries-io` MCP server is a robust and fast service designed to provide geographical boundary data for Canadian postal codes, including FSA (Forward Sortation Area) and LDU (Local Delivery Unit) levels. This server is intended to be integrated programmatically into applications and systems to enhance location-based functionalities, such as geofencing, geolocation, and navigation.

Over the past five years, the `ca-boundaries-io` service has gained the trust of over 600 clients across multiple sectors, including marketing, emergency response, insurance, and transportation. These clients rely on our service for its reliability and the comprehensive geographical data it provides. Each subscription plan includes 24x7 support, ensuring you have assistance whenever needed.

## Features

- **CA Postal Code Boundaries**: Access geographical boundaries for Canadian postal codes at both FSA and LDU levels.
- **GeoJson Integration**: Easily integrate GeoJson boundary data into your applications.
- **High Performance**: Designed for optimal performance when used programmatically.

## Tool List

### Query by FSA Code
- **Function**: `query_by_fsa_code`
  - **Description**: Retrieve boundary data by Postal FSA (e.g., T6H).

### Query by LDU Code for H3 Poly.
- **Function**: `query_for_ldu_boundary_by_location_and_resolution`
  - **Description**: Obtain LDU H3 Boundary data by specifying location and resolution.
- **Function**: `query_for_ldu_boundary_by_h3index`
  - **Description**: Query for Boundary by H3Index. If an LDU Postal Code does not exist within the H3 Index Hexagon, an empty FeatureCollection is returned. **H3Index resolution must be greater than 8.**
- **Function**: `query_for_ldu_boundary`
  - **Description**: Retrieve boundary data by LDU Postal Code.

### Query for City or Province
- **Function**: `query_for_city_names_by_province_territory_name`
  - **Description**: Retrieve city names by province or territory name.
- **Function**: `query_for_city_boundary_by_city_name`
  - **Description**: Obtain city boundary data by city name.
- **Function**: `query_for_all_province_territory_names`
  - **Description**: Retrieve all province or territory names.

## Usage

The `ca-boundaries-io` MCP server is designed to be user-friendly, allowing developers to seamlessly integrate boundary data into their applications. With its comprehensive toolset, it supports a wide range of queries, ensuring you can access the precise geographical data you need.

Explore the server's capabilities and leverage its tools to enhance your application's geolocation and boundary-related functionalities.

---

For more information or to get started, please consult the tool documentation and integrate the server into your system for a robust and efficient geographical data solution.