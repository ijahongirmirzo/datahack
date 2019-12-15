from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from sklearn.externals import joblib
gbr = joblib.load('model.pkl')


class ProductRefreshApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        post_data = request.data
        price_pred = gbr.predict({
            'company': post_data.get('company'),
            'mark': post_data.get('company'),
            'year_model': post_data.get('year_model'),
            'divigatel_hajmi': post_data.get('divigatel_hajmi'),
            'fuel_type': post_data.get('fuel_type'),
            'kuzov_type': post_data.get('kuzov_type'),
            'uzatish_qutisi': post_data.get('uzatish_qutisi'),
            'color': post_data.get('color'),
        })[0]
        return Response(status=204)

