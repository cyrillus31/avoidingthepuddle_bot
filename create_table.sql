CREATE TABLE IF NOT EXISTS video_urls (
	video_id SERIAL PRIMARY KEY,
	title VARCHAR(255) NULL,
	url VARCHAR(255) NOT NULL UNIQUE,
	upload_date DATE DEFAULT Now()::DATE
);

-- INSERT INTO video_urls (
-- 	url
-- ) VALUES (
-- 	'https://www.youtube.com/watch?v=3Yz3NlMN7LQ'
-- );


	

