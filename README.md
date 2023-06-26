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
- [🔍 Creating Filters](#-creating-filters)
- [📤 Exporting Data](#-exporting-data)
- [🎓 Conclusion](#-conclusion)

## 🚀 Buat Tabel di DynamoDB

<p>
  Login terlebih dahulu ke dalam akun AWS masing-masing, lalu masuk ke service <b>Database > DynamoDB</b>
</p>
![dynamo](https://github.com/mohlutfifadilah/aws-dynamoDB/blob/master/gambar/dynamo.png)
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

'''
In this section, we'll import data into DynamoDB using a CSV file. Let's dive in:

1. Create an S3 bucket to store the CSV file. 📦
2. Upload the CSV file to the S3 bucket. 🚀
3. Set up an IAM role and Lambda function to access DynamoDB and S3 services. 🛠️
4. Configure the Lambda function with the provided code. ⌨️
5. Test the Lambda function to import the data into DynamoDB. 🧪

For a step-by-step guide and helpful code snippets, refer to the [📥 Importing Data](#-importing-data) section of this tutorial.

## 💡 Working with DynamoDB

Now that our data is imported, let's unleash the power of DynamoDB! We'll perform various operations, including querying, updating, and deleting items. Additionally, we'll learn how to create filters to retrieve specific data based on conditions. 🗃️

To become a DynamoDB master, head over to the [💡 Working with DynamoDB](#-working-with-dynamodb) section of this tutorial.

## 🔍 Creating Filters

Filters allow us to dive deep into our data and retrieve only what we need. In this section, we'll uncover the secrets of creating filters to fetch relevant data from the DynamoDB table. Let's sharpen our query skills! 🔍

To unravel the mysteries of creating filters, refer to the [🔍 Creating Filters](#-creating-filters) section of this tutorial.

## 📤 Exporting Data

Sharing is caring! Exporting data from DynamoDB opens up endless possibilities, from backups to advanced analysis. Let's learn how to export data to different formats and take our insights to new heights. 📈

For a comprehensive guide on exporting data from DynamoDB, check out the [📤 Exporting Data](#-exporting-data) section of this tutorial.

## 🎓 Conclusion

Congratulations on conquering the Big Data and Cloud Computing Practicum! You've unlocked the secrets of DynamoDB, S3, and Lambda, empowering yourself with the skills needed to tackle Big Data challenges in the cloud. Your journey has just begun! 🚀

Feel free to explore more advanced topics, experiment with different datasets, or adapt this tutorial to suit your needs. If you have any questions or need assistance, don't hesitate to reach out. Happy cloud adventures! ⚡️✨

<p align="center">
  <img src="https://your-image-url" alt="Big Data and Cloud Computing Practicum" width="500">
</p>
