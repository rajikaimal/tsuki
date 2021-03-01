# a very approach - orchestrator registers runtimes created (in-memory)
# won't support server failtures initially as this is in-memory :P
# a hashmap saves the container metadata
# when a session is terminated, remove it from hashmap

class Orchestrator:
    __instance = None
    runtimes = {}
    def __init__(self):
        print("Init orchestrator")

    # always return the singleton
    def get_instance(self):
        if Orchestrator.__instance != None:
            raise Exception("Orchestrator is a singleton")
        else:
            Orchestrator.__instance = self

    # add to runtimes dictionary
    def add_runtime(self, runtime):
        runtimes[runtime.id] = runtime.metadata
    
    # remove from runtimes dictionary
    def remove_runtime(self, runtime_id):
        runtimes.pop(runtime_id)