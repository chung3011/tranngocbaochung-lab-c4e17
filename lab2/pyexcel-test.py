import pyexcel

data=[
{
"Name":"Huyen",
"Age":23
},
{
"Name":"Huy",
"Age":25
},
{
"Name":"Huynh",
"Age":21
}
]

pyexcel.save_as(records=data,dest_file_name="test.xlsx")
