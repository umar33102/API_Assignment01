from fastapi import FastAPI

app=FastAPI()

student = [
    {"id":1,"name":"umar","rollNo":123,"subject":"math"},
    {"id":2,"name":"hayat","rollNo":456,"subject":"urdu"}
]

# get operation
@app.get("/getData")

def getStudents():
    return f"Get Student: {student}"


# post operation
@app.post("/postData")

def postStudents():
    data = student.append({"id":4,"name":"zain","rollNo":789,"subject":"eng"})

    return "postData:", student


# put operation
@app.put("/puttData")

def putStudents():
    data = student[2]
    data["id"] =3
    return "postData:", student


# delete operation
@app.delete("/deleteData")

def deleteStudents():
    data = student.pop()
    return "deleteData:", student

