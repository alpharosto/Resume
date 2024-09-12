from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer
from .models import Candidate
from pyresparser import ResumeParser

class ResumeExtractView(APIView):
    def post(self, request, *args, **kwargs):
        template_name = 'home.html'
        file = request.FILES.get('resume')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Parse the resume
        data = ResumeParser(file).get_extracted_data()

        # Extract required fields
        first_name = data.get('name').split()[0] if data.get('name') else None
        email = data.get('email')
        mobile_number = data.get('mobile_number')

        # Save to DB
        candidate = Candidate(first_name=first_name, email=email, mobile_number=mobile_number)
        candidate.save()

        # Serialize and return response
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
