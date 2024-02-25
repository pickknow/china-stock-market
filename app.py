from flask import Flask, request
import akshare as ak
import json

app = Flask(__name__)

def pa_to_jason(df, orient='split'):
    df_json = df.to_json(orient = orient, force_ascii = False)
    return json.loads(df_json)


@app.post("/ak_fetch")
def ak_fetch():
    obj_data = request.json
    call_func = getattr(ak, obj_data['call_func'])
    try:
        result = call_func() if not obj_data['data'] else call_func(**obj_data['data'])
        return pa_to_jason(result)
    except:
        raise Exception(500)

    


