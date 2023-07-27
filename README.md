# reproducer-03573017

```
oc new-project reproducer-03573017
oc new-app https://github.com/gmeghnag/reproducer-03573017.git -n reproducer-03573017
// wait for a few minutes for the image to be built and the pod running
oc expose svc/reproducer-03573017 -n reproducer-03573017
curl -X POST -skL http://$(oc get route -n reproducer-03573017 reproducer-03573017 -o jsonpath='{.spec.host}')/model/dollyv2/instruct_generate
```
