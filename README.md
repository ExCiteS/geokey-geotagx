# geokey-geotagx

Import results from GeoTag-x.

## API

To import results post a feature collection:

```
POST /api/geotagx/import/
Content-Type: application/json

{
    "type": "FeatureCollection",
    "features": []
}
```

Returns (if successful):

```
HTTP/1.1 201 Created

Objects created
```
