/*
 Navicat Premium Data Transfer

 Source Server         : flask
 Source Server Type    : MySQL
 Source Server Version : 50739 (5.7.39-log)
 Source Host           : localhost:3306
 Source Schema         : hello

 Target Server Type    : MySQL
 Target Server Version : 50739 (5.7.39-log)
 File Encoding         : 65001

 Date: 30/09/2022 23:32:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hi
-- ----------------------------
DROP TABLE IF EXISTS `hi`;
CREATE TABLE `hi`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1246 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hi
-- ----------------------------
INSERT INTO `hi` VALUES (1, 'qwe');
INSERT INTO `hi` VALUES (2, 'hadoop');
INSERT INTO `hi` VALUES (20, '狂神');
INSERT INTO `hi` VALUES (22, '王w伟');
INSERT INTO `hi` VALUES (23, '张三');
INSERT INTO `hi` VALUES (1243, 'hahah');
INSERT INTO `hi` VALUES (1244, 'flask');
INSERT INTO `hi` VALUES (1245, 'pandas');

SET FOREIGN_KEY_CHECKS = 1;
