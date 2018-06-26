import sixtracktools

six =sixtracktools.SixTrackInput('.')
line,rest, iconv =six.expand_struct()


beam=sixtracktools.SixDump3('dump3.dat')
fb=beam.get_full_beam()

print("# SixTrackLib Elements")
for ic,el in enumerate(line):
    print(ic,":",el)


print("# SixTrack SixTrackLib")
for ic,el in enumerate(line):
    print(ic,"->",el)

print("#initial condition particle 1")
for ll in sorted(fb):
    dt=fb[ll]
    if hasattr(dt,'__len__'):
       print(ll,dt[0])
    else:
       print(ll,dt)


print("#initial condition particle 2")

for ll in sorted(fb):
    dt=fb[ll]
    if hasattr(dt,'__len__'):
       print(ll,dt[1])
    else:
       print(ll,dt)




