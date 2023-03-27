CREATE DATABASE CHARACTER SET utf_8 IF NOT EXISTS logger;

USE logger;

CREATE TABLE IF NOT EXISTS request_logs (
    id BIGINT NOT NULL AUTO_INCREMENT,
    request_token CHAR(127),
    request_body JSON,
    request_query JSON,
    which_system TINYINT(1) NOT NULL COMMENT '1 => Node JS SERVER; 2 => CRM Logs',
    base_url CHAR(255) NOT NULL,
    headers TEXT NOT NULL,
    method ENUM('GET', 'POST', 'PUT', 'DELETE', 'HEAD'),
    response_body TEXT NOT NULL,
    sender_ip_address CHAR(63) NOT NULL,
    user_id BIGINT,
    is_error TINYINT(1) NOT NULL,
    status CHAR(4) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY(id)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS mobile_logs (
    id BIGINT NOT NULL AUTO_INCREMENT,
    error_code TINYINT,
    stack_tree TEXT,
    error_type TEXT,
    os ENUM('ios', 'android', 'web'),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY(id)
) ENGINE=MyISAM;

SHOW TABLES;