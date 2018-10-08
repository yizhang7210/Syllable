package com.syllable.exchange.controllers;

import com.syllable.exchange.dtos.PredictionDto;
import com.syllable.exchange.services.PredictionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
@RequestMapping("/predictions")
public class PredictionController {

    @Autowired
    private PredictionService predictionService;

    @RequestMapping(method = RequestMethod.POST)
    public PredictionDto createPrediction(@RequestBody PredictionDto predictionBody) {
        return predictionService.createPrediction(predictionBody);
    }

    @RequestMapping(method = RequestMethod.GET)
    public String getPredictions() {
        return "All Predictions";
    }

}