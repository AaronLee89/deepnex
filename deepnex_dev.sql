/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : deepnex_dev

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2017-11-04 10:42:44
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
INSERT INTO `alembic_version` VALUES ('8294b00f5265');

-- ----------------------------
-- Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `content` text NOT NULL,
  `visitNum` int(11) DEFAULT NULL,
  `updatedTime` datetime DEFAULT NULL,
  `poster` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('2', '中国共产党的第十九次全国代表大会', '<p>\r\n\r\n</p><div>中国共产党第十九次全国代表大会（简称党的十九大）于2017年10月18日至10月24日在北京召开。</div><div><br></div><div><b>2017年10月18日上午9:00，中国共产党第十九次全国代表大会在人民大会堂开幕。</b>习近平代表第十八届中央委员会向大会作了题为《决胜全面建成小康社会 夺取新时代中国特色社会主义伟大胜利》的报告。</div><div><br></div><div>这次大会的主题是：不忘初心，牢记使命，高举中国特色社会主义伟大旗帜，决胜全面建成小康社会，夺取新时代中国特色社会主义伟大胜利，为实现中华民族伟大复兴的中国梦不懈奋斗。</div>\r\n\r\n<br><p></p>', '3', '2017-11-04 00:39:47', '邹哲鹏');
INSERT INTO `news` VALUES ('3', '炉石传说法师新卡：传说武器-艾露尼斯', '<p>暴雪嘉年华内容大公布，小编先来给你划重点：</p><p>地下城冒险：免费单人地下城冒险，官方套牌；九职业橙武：传说武器牌(据说会免费送一把？)；</p><p>新关键词：招募；新卡背：为了财富、蜡烛之王；新棋盘、新故事；总计135张新卡牌！</p><p>上线时间：预计为2017年12月。\r\r<br></p><p><img alt=\"\" src=\"http://03.imgmini.eastday.com/mobile/20171104/20171104081211_14a97b045f17aa7b27aab1d9bc9242d0_1.jpeg\"><br></p>', '1', '2017-11-04 10:03:48', '旅法师营地');

-- ----------------------------
-- Table structure for `notices`
-- ----------------------------
DROP TABLE IF EXISTS `notices`;
CREATE TABLE `notices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `content` text NOT NULL,
  `visitNum` int(11) DEFAULT NULL,
  `updatedTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of notices
-- ----------------------------

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
  `real_name` varchar(128) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `permissions` int(11) NOT NULL,
  `is_auth` int(11) NOT NULL,
  `avatar_url` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'admin', 'pbkdf2:sha1:1000$wAiUd6RQ$32d991e70c56098f0de9e81884266690024a822a', 'admin@qq.com', null, null, null, null, '2017-11-02 20:58:42', '2017-11-02 20:58:42', '0', '0', '/static/resource/img/none.jpg');
