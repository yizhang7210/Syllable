package com.syllable.exchange.daos;

import com.syllable.exchange.models.SyllableUser;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SyllableUserDao extends MongoRepository<SyllableUser, String> {

    SyllableUser findByUsername(String username);

}
