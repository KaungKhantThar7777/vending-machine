import os
import pandas as pd
import graphene
from django.conf import settings

class CSVRowType(graphene.ObjectType):
    data = graphene.JSONString()

class Query(graphene.ObjectType):
    csv_to_json = graphene.List(CSVRowType)

    def resolve_csv_to_json(self, info):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'api', 'api-test.csv')

            df = pd.read_csv(file_path)

            json_data = df.to_dict(orient="records")

            return [CSVRowType(data=row) for row in json_data]

        except Exception as e:
            return [CSVRowType(data={"error": str(e)})]

schema = graphene.Schema(query=Query)
