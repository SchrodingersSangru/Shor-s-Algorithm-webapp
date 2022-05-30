from django.http import JsonResponse
from django.shortcuts import render
import json

from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('1689c0f13c06463b86a0b97b3352ae05161342194008f6e1dc4c6330d36ba60f646b018f37dcc745da8d683e18f327fa418539589201d22abc38bd635c47ac9d')
provider = IBMQ.get_provider(hub='ibm-q')

def home(request):
    return render(request, 'index.html', {})

def factor(request):

    print(request.body)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode);

    device = body['device']
    number = int(body['number'])

    backend = provider.get_backend(device)

    factors = Shor(QuantumInstance(backend, shots=1, skip_qobj_validation=False)) #Function to run Shor's algorithm where 21 is the integer to be factored

    result_dict = factors.factor(N=number, a=2)
    result = result_dict.factors

    response = JsonResponse({'result': str(result)})
    return response