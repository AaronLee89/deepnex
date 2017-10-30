/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : deepnex_dev

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2017-10-30 09:08:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('7bc09a268523');

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `permissions` int(11) NOT NULL,
  `avatar_url` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `real_name` varchar(128) DEFAULT NULL,
  `is_auth` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'zzp', 'pbkdf2:sha1:1000$cr2kZAgW$ad6f49af5affb11dcaa684e9a37cc2f241dd38ed', '503951764@qq.com', null, '2017-10-29 15:24:14', '2017-10-18 16:17:51', '1', '/static/upload/avatar/1.png?t=1508738497.85', '中山大学数据科学与计算机学院', '13802401913', '邹哲鹏', '0');
INSERT INTO `users` VALUES ('2', 'zhangziye', 'pbkdf2:sha1:1000$65zn9NiN$1eb564ee7e2b58695140b55ae0d2d4fae1535012', '123@qq.com', null, '2017-10-26 19:07:15', '2017-10-26 19:07:05', '1', '/static/resource/img/none.jpg', null, null, null, '1');
INSERT INTO `users` VALUES ('3', 'admin', 'pbkdf2:sha1:1000$WWNDowLT$5a8d092e177be0a669d926fc807bfee26afe19c7', 'admin@qq.com', null, '2017-10-29 15:39:22', '2017-10-28 15:57:03', '0', '/static/resource/img/none.jpg', null, null, null, '1');
INSERT INTO `users` VALUES ('4', 'zouzhp', 'pbkdf2:sha1:1000$Et120bf9$fa5d2ec6af58f90faa8a67cff7f0bc43db4fdce0', '1234@qq.com', null, '2017-10-29 15:35:29', '2017-10-29 15:35:29', '1', '/static/resource/img/none.jpg', null, null, null, '0');
