/* STANLEY: This code now accesses the db on GTER using my login.
* This code will set up the database on GTER, even though it's run from this
* computer. It will also call a later file to start actual data gathering.
*/
const express = require('express');
const mysql = require('mysql');

// Create connection
const db = mysql.createConnection({
    host    : '192.168.1.156',
    user    : 'pmhalvor',
	password: '*****',
	database: 'guests'
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
/*
* Here, you'll have to start by building the database.
* I'm still using express because that's the only way I've seen it done.
* When I get this working, I can start exploring other options.
* Hopefully in Javascrript, the code will just run automatically! Or, more
* directly, at least.
*
*
*/
app.get('/createdb', (req, res) => {
    let sql = 'CREATE DATABASE guests';
    db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Database created...');
		// res.send(result);
    })
});
// You can just leave this uncommented

// Create table
app.get('/createinfotable', (req, res) =>{
    let sql = 'CREATE TABLE info(id int AUTO_INCREMENT, name VARCHAR(255), age int, weight float, PRIMARY KEY(id))';
    db.query(sql, (err, result)=>{
        if(err) throw err;
        console.log(result);
        res.send('Info table created...');
		// res.send(result);
    })
});
// Done for now. Don't need to run these anymore.









//whatever port you like
app.listen('3001', () => {
    console.log('Server started on port 3001, baby.')
});



//                           THE GRAVEYARD




//
//
// //Insert post 1
// app.get('/addpost1', (req, res) =>{
	//     let post = {title: 'Post One', body:' This post is number one'};
	//     let sql = 'INSERT INTO posts SET ?';
	//     let query = db.query(sql, post, (err, result) =>{
		//         if(err) throw err;
		//         console.log(result);
		//         res.send('Post 1 added...');
		//     })
		// })
		//
		//
		// //Insert post 21
		// app.get('/addpost2', (req, res) =>{
			//     let post = {title: 'Post Two', body:' This post is number two'};
			//     let sql = 'INSERT INTO posts SET ?';
			//     let query = db.query(sql, post, (err, result) =>{
				//         if(err) throw err;
				//         console.log(result);
				//         res.send('Post 2 added...');
				//     })
				// })
				//
				//
				// // Select posts
				// app.get('/getposts', (req, res) => {
					//     let sql = 'SELECT * FROM posts';
					//     let query = db.query(sql, (err, results)=>{
						//         if(err) throw err;
						//         console.log(results);
						//         res.send('Posts fetched...');
						//     })
						// })
						//
						// // Select single post
						// app.get('/getpost/:id', (req, res) => {
							//     let sql = `SELECT * FROM posts WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
							//     let query = db.query(sql, (err, result)=>{
								//         if(err) throw err;
								//         console.log(result);
								//         res.send('Post fetched...');
								//     })
								// })
								//
								//
								// // Update
								// app.get('/updatepost/:id', (req, res) => {
									//     let newTitle = 'Updated Title';
									//     let sql = `UPDATE posts SET title = '${newTitle}' WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
									//     let query = db.query(sql, (err, result)=>{
										//         if(err) throw err;
										//         console.log(result);
										//         res.send('Post updated...');
										//     })
										// })
										//
										//
										// // Delete post
										// app.get('/deletepost/:id', (req, res) => {
											//     let sql = `DELETE FROM posts WHERE id = ${req.params.id}`; // NOTICE THE DIFFERENT APOSTROPHES HERE!
											//     let query = db.query(sql, (err, result)=>{
												//         if(err) throw err;
												//         console.log(result);
												//         res.send('Post deleted...');
												//     })
												// })
												//





// END OF FILE
