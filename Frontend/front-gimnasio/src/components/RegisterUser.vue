<template id="formUsuario">
    <div class="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
    <div class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
        <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
            <div class="mt-12 flex flex-col items-center">
                
                <div class="w-full flex-1 mt-8 grid-cols-2">
                    <div class="gap-1">
                            <Usuario></Usuario>
                            <Persona></Persona>
    
                            

                            <p class="mt-6 text-xs text-gray-600 text-center col-span-2">
                                I agree to abide by templatana's
                                <a href="#" class="border-b border-gray-500 border-dotted">
                                    Terms of Service
                                </a>
                                and its
                                <a href="#" class="border-b border-gray-500 border-dotted">
                                    Privacy Policy
                                </a>
                            </p>
                    </div>
                </div>
            </div>
        </div>
 
    </div>
</div>
</template>

<script>
    import Persona from './Persona.vue';
    import Usuario from './Usuario.vue';

    export default {
        components: {
            Persona,
            Usuario
        }
    }

</script>