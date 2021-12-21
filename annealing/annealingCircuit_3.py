import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

####################################
## time         1: work in time
##              0: work out of time
##
## location     1: presential
##              0: remote
##
## length       1: short
##              0: long
##
## mandatory    1: obligatory
##              0: optional
####################################

sampler = EmbeddingComposite(DWaveSampler()) # sampler
# sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000Q_6'))
# sampler = EmbeddingComposite(DWaveSampler(solver=dict(topology__type='pegasus')))

def scheduling(time, location, length, mandatory):

    if time: # work in time
        return (location and mandatory)

    else: # work out of time
        return (not location and not length)


csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(scheduling, ['time', 'location', 'length', 'mandatory'])


bqm = dwavebinarycsp.stitch(csp)
# print(bqm.linear)
# print(bqm.quadratic)

response = sampler.sample(bqm, num_reads = 5000)
min_energy = next(response.data(['energy']))[0]

print(response)

print('-----------')

total = 0

for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    total = total + occurences

    time = 'business hours' if sample['time'] else 'evenings'
    location = 'office' if sample['location'] else 'home'
    length = 'short' if sample['length'] else 'long'
    mandatory = 'mandatory' if sample['mandatory'] else 'optional'

    print("{}: During {} at {}, you can schedule a {} meeting that is {}".format(occurences, time, location, length, mandatory))