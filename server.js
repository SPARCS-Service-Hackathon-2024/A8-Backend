const express = require('express');
const http = require('http');
const socketio = require('socket.io');
const mysql = require('mysql');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

// MySQL 연결 설정
const db = mysql.createConnection({
  host: 'ec2-3-139-216-27.us-east-2.compute.amazonaws.com',
  user: 'root', // 로컬 MySQL 사용자 이름
  password: 'password', // 로컬 MySQL 비밀번호
  database: '2024SparcsHackathon' // 사용할 데이터베이스 이름
});

// 데이터베이스 연결
db.connect(err => {
  if (err) {
    console.error('데이터베이스 연결 오류: ', err);
    return;
  }
  console.log('데이터베이스 연결 성공!');
});

// WebSocket 연결 처리
io.on('connection', socket => {
  console.log('새로운 클라이언트가 연결되었습니다.');

  // 채팅 관련 이벤트 처리
  socket.on('joinRoom', data => {
    // 방에 참가하는 로직 구현
  });

  socket.on('leaveRoom', data => {
    // 방에서 나가는 로직 구현
  });

  socket.on('chatMessage', msg => {
    // 채팅 메시지를 받아 처리하는 로직 구현
    io.emit('message', msg); // 모든 클라이언트에게 메시지 전송
  });

  socket.on('disconnect', () => {
    console.log('클라이언트가 연결을 끊었습니다.');
  });
});

// Express 라우터 설정 (회원가입, 방 관리 등)

app.get('/', (req, res) => {
  res.send('채팅 앱 서버');
});

// 서버 시작
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`서버가 ${PORT}번 포트에서 실행 중입니다.`);
});
