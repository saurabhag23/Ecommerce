from django.db import IntegrityError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call the default exception handler first, to get the standard error response.
    response = exception_handler(exc, context)
    
    # Handle cases where the default exception handler does not create a response.
    if response is None:
        # Check if the exception is an IntegrityError, which often occurs from duplicate data.
        if isinstance(exc, IntegrityError):
            # Return a 409 CONFLICT response indicating that there was an integrity error.
            return Response({'detail': 'Integrity error, possibly duplicate data.'}, status=status.HTTP_409_CONFLICT)

    else:
        # Modify the response to add additional information if the error is related to the 'name' field.
        if 'name' in response.data:
            response.data['name_help'] = "Ensure the name is unique and meets all specified rules."
    
    # Return the modified response or the default one if no modifications were made.
    return response
