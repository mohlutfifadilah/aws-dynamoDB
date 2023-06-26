<h1 align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=aws&theme=light" />
  </a>
</h1>

<h1>Import CSV ke dalam AWS menggunakan DynamoDB</h1>

<p>
  Selamat datang, langkah-langkah ini akan mamandu anda untuk mengimport CSV ke dalam AWS menggunakan DynamoDB, semoga dapat membantu anda. Let's level up your cloud skills! 💪
</p>

## 📚 Daftar Isi :

- [🚀 Buat Tabel di DynamoDB](#-Buat-Tabel-di-DynamoDB)
- [✨ Import CSV](#-Import-CSV)
- [🎉 Buat Role](#-Buat-Role)
- [📥 Tambahkan Permission Policies](#-Tambahkan-Permission-Policies)
- [💡 Working with DynamoDB](#-working-with-dynamodb)
- [🔍 Tambahkan Filter](#-Tambahkan-Filter)
- [📤 Export Data](#-Export-Data)
- [🎓 Conclusion](#-conclusion)

## 🚀 Buat Tabel di DynamoDB

<p>
  Login terlebih dahulu ke dalam akun AWS masing-masing, lalu masuk ke service <b>Database > DynamoDB</b>
</p>
![dynamo](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/dynamo.png)
![dynamo](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/dynamo.png?raw=true)

<p>
  Lalu buat table dengan klik <b>Create Table</b>, lalu isikan kolom apa saja yang dibutuhkan beserta tipe datanya lalu klik Create Table
</p>
![create-table](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/create-table.png)
![table-detail](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/table-detail.png)
<p>
  Jika sudah, cek apakah tabel sudah aktif atau belum, bila sudah akan terdapat tampilan seperti dibawah ini
</p>
![active-table](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/active-table.png)


In this tutorial, we'll embark on a thrilling journey of Big Data and Cloud Computing using AWS services. DynamoDB will be our trusted NoSQL database, while S3 will provide storage power. We'll leverage the incredible capabilities of AWS Lambda functions to process and analyze data. Let's unleash the true potential of the cloud! ☁️

## ✨ Import CSV

<p>
  Masuk ke menu <b>Bucket</b>, lalu <b>Create Bucket</b>
</p>
![create-bucket](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/create-bucket.png)
<p>
  Jika sudah, akan muncul pesan berhasil
</p>
![upload-csv-to-bucket](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/upload-csv-to-bucket.png)

## 🎉 Buat Role

<p>
  Setelah file csv berhasil di upload, buat Role terlebih dahulu masuk ke menu <b>Identity and Access Management (IAM) > Roles > Create Role</b>
</p>
![create-role](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/create-role.png)
<p>
  Lalu buat function lambda 
</p>
![create-lambda-function](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/create-lambda-function.png)

## 📥 Tambahkan Permission Policies

<p>
  Buka tab Permission Policies pada function lambda yang dibuat tadi
  a.  AmazonDynamoDBFullAccess
  b.  AmazonS3FullAccess
</p>
![add-permission-policy](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/add-permission-policy.png)
<p>
  Setelah itu, buat function lambda beserta code programnya
</p>
![lambda-function](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/lambda-function.png)
<p>
  Lalu tambahkan Role yang sudah tadi dibuat
</p>
![existing-role](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/existing-role.png)
<p>
  Tambahkan code berikut ini pada function yang sudah tadi dibuat atau yang akan kita run untuk import file csv
</p>
'''python
import boto3
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("profile")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    Students = data.split("\n")
    #print(friends)
    for friend in Students:
        print(friend)
        friend_data = friend.split(";")
        # add to dynamodb
        try:
            table.put_item(
                Item = {
                    "nim"       : friend_data[0],
                    "nama"      : friend_data[1]
                }
            )
        except Exception as e:
            print("e")
'''
<p>
  Lalu masuk ke menu <b>Configuration > General Configuration > Edit</b>, lalu ubah timeout menjadi 2 menit
</p>
![add-timeout](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/add-timeout.png)
<p>
  Lalu test dengan klik <b>Test</b>
</p>
![test-event](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/test-event.png)
<p>
  Masukkan kode JSON pada event nya
</p>
![add-json](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/add-json.png)
'''json
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "s1sd-s3",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::s1sd-s3"
        },
        "object": {
          "key": "s1sd.csv",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
'''

<p>
  Cek items dari apakah sudah terimport atau belum, jika sudah item akan muncul
</p>
![check](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/check.png)

## 🔍 Tambahkan Filter

<p>
  Tambahkan filter pada tabel
</p>
![add-filter](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/add-filter.png)

## 📤 Export Data

<p>
  Untuk export data, klik pada menu <b>Action > Download result to CSV</b> 
</p>
![export-result](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/export-result.png)

Selamat ! Anda telah membuka rahasia DynamoDB, S3, dan Lambda, memberdayakan diri Anda dengan keterampilan yang diperlukan untuk mengatasi tantangan Big Data di Cloud. Perjalanan Anda baru saja dimulai! 🚀

Jangan ragu untuk menjelajahi topik yang lebih lanjut, bereksperimen dengan set data yang berbeda, atau sesuaikan tutorial ini dengan kebutuhan Anda. Jika Anda memiliki pertanyaan atau memerlukan bantuan, jangan ragu untuk menghubungi kami. Selamat berpetualang di awan! ⚡️✨

<p align="center">
  <img src="https://your-image-url" alt="Big Data and Cloud Computing Practicum" width="500">
</p>
