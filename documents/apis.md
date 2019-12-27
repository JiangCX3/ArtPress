# Artpress API
Artpress Public APIs

* [Media Library](#media-library)
    * [`api/medialib/getmymedias/`](#apimedialibgetmymedias)
    * [`api/medialib/getmedias/`](#apimedialibgetmedias)

## Media Library

### `api/medialib/getmymedias/`
Get logged user all medias.

#### Param
Method: `Post`

args  | type | explanation       | can be NULL
---   | ---  | ---               | ---
token | str  | django csrf token | false

#### Return

```json
{
    "code": 200,
    "user": "username",
    "data": [
        {
            "id": 10,
            "author": {
                "uid": 1,
                "name": "username"
            },
            "res": "https://.../picture.jpg",
            "thum": "http://.../picture.jpg?thumbnails=true",
            "update_time": "1970-1-1 00:00:00"
        },
 
        ...

    ]
}
```

#### Code
code | explanation
---  | ---
200  | Successfully 
401  | User is not logged

----------------------------------------


### `api/medialib/getmedias/`
Get somebody medias.
#### Param
Method: `Post`

args  | type | explanation       | can be NULL
---   | ---  | ---               | ---
token | str  | django csrf token | false
uid   | int  | object user id    | false

#### Return

```json
{
    "code": 200,
    "user": "username",
    "data": [
        {
            "id": 10,
            "author": {
                "uid": 1,
                "name": "username"
            },
            "res": "https://.../picture.jpg",
            "thum": "http://.../picture.jpg?thumbnails=true",
            "update_time": "1970-1-1 00:00:00"
        },
 
        ...

    ]
}
```

#### Code
code | explanation
---  | ---
200  | Successfully 
401  | User is not logged

----------------------------------------


