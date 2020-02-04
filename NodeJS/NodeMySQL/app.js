// This file uses Node to handle SQL queries in a MySQL database.
// I want to use this for data entry on my website
// In order to do that, I'll have to host the app from my home server.
// This is a great example code though!


/* STANLEY: This code now accesses the db on GTER using my login.
// 			That means I need to:
// 				create a guest account on the db
				delete my password from this one

*/
const express = require('express');
const mysql = require('mysql');

// Create connection
const db = mysql.createConnection({
    host    : '192.168.1.156',
    user    : 'guest',
	password: '*******',
    database:'gter'
});

// Connect
db.connect((err)=>{ 
    if(err){
        throw err;
    }
    console.log('MySQL Connected...');
});

const app = express();

// Create db
app.get('/createdb', (req, res) => {
    let sql = 'CREATE DATABASE nodemysqlsecond';
    db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Database created...');

    })
})
// You can just leave this uncommented

// Create table
app.get('/createposttable', (req, res) =>{
    let sql = 'CREATE TABLE post(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id))';
    db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Post table created...');
    })
});


//Insert post 1
app.get('/addpost1', (req, res) =>{
    let post = {title: 'Post One', body:' This post is number one'};
    let sql = 'INSERT INTO posts SET ?';
    let query = db.query(sql, post, (err, result) =>{
        if(err) throw err;
        console.log(result);
        res.send('Post 1 added...');
    })
})


//Insert post 21
app.get('/addpost2', (req, res) =>{
    let post = {title: 'Post Two', body:' This post is number two'};
    let sql = 'INSERT INTO posts SET ?';
    let query = db.query(sql, post, (err, result) =>{
        if(err) throw err;
        console.log(result);
        res.send('Post 2 added...');
    })
})


// Select posts
app.get('/getposts', (req, res) => {
    let sql = 'SELECT * FROM posts';
    let query = db.query(sql, (err, results)=>{
        if(err) throw err;
        console.log(results);
        res.send('Posts fetched...');
    })
})

// Select single post
app.get('/getpost/:id', (req, res) => {
    let sql = `SELECT * FROM posts WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
    let query = db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Post fetched...');
    })
})


// Update
app.get('/updatepost/:id', (req, res) => {
    let newTitle = 'Updated Title';
    let sql = `UPDATE posts SET title = '${newTitle}' WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
    let query = db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Post updated...');
    })
})


// Delete post
app.get('/deletepost/:id', (req, res) => {
    let sql = `DELETE FROM posts WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
    let query = db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Post deleted...');
    })
})








//whatever port you like
app.listen('3000', () => {
    console.log('Server started on port 3000, baby.')
});













// END OF FILE
