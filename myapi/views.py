
# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Question,Answer
from .serializers import QuesSerializer,AnsSerializer


 
#home
@api_view(['GET'])
def Info(request):
    return Response({"info":"welcome to question answer api"},status=status.HTTP_200_OK)
 
#This is Getquestions/ route only register user can see the question 
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Getquestion(request):
    allquestion=Question.objects.all()
    serilizr=QuesSerializer(allquestion,many=True)
    return Response(serilizr.data,status=status.HTTP_200_OK)


#This is Createquestion/ route only  admin can create the question 
@api_view(['POST'])
@permission_classes((IsAuthenticated,IsAdminUser))
def CreatQuestion(request):
    serilizer=QuesSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response({"message":"Question has successful created"},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":"data format or key is wrong"},status=status.HTTP_406_NOT_ACCEPTABLE)       


#This is Getanswers/ route only  register user can see the answer
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def AnsViews(request):
    allanswer=Answer.objects.all()
    serilizr=AnsSerializer(allanswer,many=True)
    return Response(serilizr.data,status=status.HTTP_200_OK)


#This is Createanswer/ route only  user can post the answer
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def CreatAnswer(request):
    serilizer=AnsSerializer(data=request.data)
    if  request.user.is_staff:
        return Response({"error":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
         
    elif serilizer.is_valid():
        serilizer.save()
        return Response({"message":"Answer has successful posted"},status=status.HTTP_201_CREATED) 

    else:
        return Response({"error":"data format or key is wrong"},status=status.HTTP_406_NOT_ACCEPTABLE) 
       
      

 
