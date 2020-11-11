package com.example.photoblog;

import java.util.Date;

public class Comments {

    private String message, user_id;
    private Date Timestamp;

    public Comments () {

    }

    public Comments(String message, String user_id, Date timestamp) {
        this.message = message;
        this.user_id = user_id;
        Timestamp = timestamp;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }

    public Date getTimestamp() {
        return Timestamp;
    }

    public void setTimestamp(Date timestamp) {
        Timestamp = timestamp;
    }

}
