from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from dotenv import load_dotenv
import os


load_dotenv()
api_token = os.getenv("IBM_API_TOKEN")

service = QiskitRuntimeService(channel="ibm_quantum", token=api_token)


backend = service.backend("ibm_brisbane")


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Transpiler le circuit pour le backend cib
transpiled_circuit = transpile(qc, backend=backend, optimization_level=3)

with Session(backend=backend) as session:

    sampler = Sampler(mode=session)
    job = sampler.run([transpiled_circuit])
    
    # Afficher l'ID du job
    print(f"Job ID: {job.job_id()}")
