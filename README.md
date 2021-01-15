# TappdIn

A python script to pipe my recent untappd checkins into an Elasticsearch index. Created to have a play around with Elastic. 

## Usage
es_http_auth_enabled = os.getenv("ES_HTTP_AUTH_ENABLED", False)
es_user = os.getenv("ES_HTTP_AUTH_USER")
es_password = os.getenv("ES_HTTP_AUTH_PASSWORD")

Set the follow environment variables. Discover how to obtain Untappd API credentials [here.](https://untappd.com/api/docs)

| Name                         | Description                            | Default          |
|------------------------------|----------------------------------------|------------------|
| UNTAPPD_USERNAME             | Untappd username to fetch for          | N/A              |
| UNTAPPD_TOKEN                | Untappd access token                   | N/A              |
| ES_HOST                      | The host address of Elasticsearch      | localhost        |
| ES_PORT                      | The port Elasticsearch is listening on | 9200             |
| ES_INDEX                     | Whether to consume basic auth creds    | false            |
| ES_HTTP_AUTH_ENABLED         | The index to stash data in             | untappd_checkins |
| ES_HTTP_AUTH_USER            | Elastic username                       | N/A              |
| ES_HTTP_AUTH_PASSWORD        | Elastic password                       | N/A              |

Source venv: `source venv/bin/activate`

Install dependencies: `pip install -r requirements.txt`

Run the script: `python3 tapped.py`
## License
[MIT](https://choosealicense.com/licenses/mit/)
