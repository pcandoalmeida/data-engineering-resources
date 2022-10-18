Memory Diagrams in Python

https://youtu.be/wAx2DgsHQg4

Nina Zakharenko - Memory Management in Python - The Basics - PyCon 2016

https://youtu.be/F6u5rhUQ6dU

Visualisation: `increase_task_count`:

Non-Global Solution:

https://pythontutor.com/visualize.html#code=task_count%20%3D%205%0A%0Adef%20increase_task_count%28task_count%29%3A%0A%20%20%20%20task_count%20%2B%3D%201%0A%20%20%20%20return%20task_count%0A%0Atask_count%20%3D%20increase_task_count%28task_count%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Global Solution:

https://pythontutor.com/render.html#code=task_count%20%3D%205%0A%0Adef%20increase_task_count%28%29%3A%0A%20%20%20%20global%20task_count%0A%20%20%20%20task_count%20%2B%3D%201%0A%0Aincrease_task_count%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
