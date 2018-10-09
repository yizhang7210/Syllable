package com.syllable.exchange.daos;

import com.syllable.exchange.models.ExchangeEvent;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventDao extends MongoRepository<ExchangeEvent, String> {
}
