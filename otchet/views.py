from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from .models import Report
from .serializers import ReportSerializer

class ReportView(APIView):
    def post(self, request):
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header and ' ' in authorization_header:
                token = authorization_header.split(' ')[1]
                decoded_token = jwt.decode(token, options={"verify_signature": False})
                user_id = decoded_token.get('user_id')

                # Проверяем, что user_id не пустой и является целым числом
                if not user_id or not isinstance(user_id, int):
                    return Response({"detail": "Некорректный user_id в токене"}, status=status.HTTP_400_BAD_REQUEST)

                # Пытаемся найти пользователя по user_id
                try:
                    user = User.objects.get(id=user_id)
                except User.DoesNotExist:
                    return Response({"detail": f"Пользователь с id {user_id} не найден"}, status=status.HTTP_404_NOT_FOUND)

                # Получаем данные отчета из request.data
                data = {
                    'user': user.id,  # Используем экземпляр модели User
                    'image_id': request.data.get('image_id'),
                    'department': request.data.get('department'),
                    'object_name': request.data.get('object_name'),
                    'assortment': request.data.get('assortment'),
                    'quantity': request.data.get('quantity'),
                }

                serializer = ReportSerializer(data=data)
                if serializer.is_valid():
                    instance = serializer.save()
                    response_data = {
                        "detail": "Данные успешно сохранены",
                        "report": {
                            "id": instance.id,
                            "user": instance.user.id,
                            "image_id": instance.image_id,
                            "department": instance.department,
                            "object_name": instance.object_name,
                            "assortment": instance.assortment,
                            "quantity": instance.quantity,
                        }
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"detail": "Введите токен в Authorization"}, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.DecodeError:
            return Response({"detail": "Ошибка декодирования токена"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
