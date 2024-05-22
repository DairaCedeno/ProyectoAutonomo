package com.example.demo.controllers;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.models.clienteModels;
import com.example.demo.services.ClienteService;

@RestController
@RequestMapping
public class ClienteController {
    @Autowired
    ClienteService clienteService;
    @GetMapping()
    public ArrayList<clienteModels> obtenerClientes(){
        return clienteService.obtenerClientes();
    }
}

@PostMapping()
public clienteModels guardarCliente(@RequestBody clienteModels cliente){
    return this.clienteService.guardarCliente(cliente);
}
