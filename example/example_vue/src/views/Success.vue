<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you :D</h1>
                <p>Yout order will be processed within 48 hours</p>
            </div>
        </div>
    </div>
</template>

<script>
export default ({
    name: 'Success',
    data() {
        return {

        }
    },
    mounted() {
        document.title = 'Success | EXAMPLE'
    }
})
</script>
