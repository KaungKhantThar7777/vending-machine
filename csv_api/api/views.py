import os
import pandas as pd
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def csv_to_json(request):
    try:
        file_path = os.path.join(settings.BASE_DIR, 'api', 'api-test.csv')
        df = pd.read_csv(file_path)
        json_data = df.to_dict()
        return Response(json_data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
